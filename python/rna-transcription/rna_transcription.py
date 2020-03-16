def to_rna(dna_strand):
    transcription = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    try:
        return ''.join([transcription[k] for k in dna_strand])
    except:
        raise ValueError('{} is not a valid DNA chain'.format(dna_strand))

