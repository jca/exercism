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

    public indexOf = (search: number, min: number = 0, max: number = -1): number => {
        if (this.array === undefined) {
            return -1;
        }

        //1. Ad-hoc behaviour when reaching end of loop
        const top = max > -1 ? max : this.array.length - 1;
        if (top <= 1) {
            switch (search) {
                case this.array[0]: return 0;
                case this.array[1]: return 1;
                default: return -1;
            }
        }

        //2. Check middle value
        const candidate = Math.ceil((min + top) / 2)

        //3. Recurse through data
        if (search < this.array[candidate]) {
            return this.indexOf(search, min, candidate - 1);
        } else if (this.array[candidate] < search) {
            return this.indexOf(search, candidate + 1, top);
        }

        //4. Return first matching value (not expected here)
        // while (candidate > 0 && this.array[candidate-1] === search) {
        //     candidate--;
        // }

        return candidate;
    }
}
