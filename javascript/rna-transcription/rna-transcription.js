// rna-transcription.js

const dnaTranscriber = function() {
  const dnaToRnaMap = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
  }

  transcribe = (nucleotide) => {
    if (nucleotide in dnaToRnaMap) {
      return dnaToRnaMap[nucleotide]
    }
    throw Error("Invalid input")
  }
}

dnaTranscriber.prototype.toRna = function(dna) {
  return [...dna].map(transcribe).join('')
}

module.exports = dnaTranscriber