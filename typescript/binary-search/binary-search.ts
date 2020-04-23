const isSortedArray = (array: number[]): boolean => {
    // Ensure that no element is less than it's predecessor
    return array.findIndex((value, index) => index > 0 && array[index - 1] > value) === -1
}

export default class BinarySearch {
    public array: number[] | undefined

    constructor(sortedData: number[]) {
        if (isSortedArray(sortedData)) {
            this.array = sortedData;
        }
    }

    public indexOf = (search: number): number => {
        return this.array ? this.search(this.array, search, 0, this.array.length - 1) : -1;
    }

    private search = (array: number[], search: number, min: number, max: number): number => {
        if (min >= max) {
            return array[max] === search ? max : -1;
        }

        const mid = Math.ceil((min + max) / 2)
        if (search < array[mid]) {
            return this.search(array, search, min, mid - 1);
        } else if (array[mid] < search) {
            return this.search(array, search, mid + 1, max);
        }
        return mid;
    }
}
