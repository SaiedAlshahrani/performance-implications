#!/bin/bash

## To run this script: ##
#$ bash glove_train.sh <wikipedia_dump_text_file> <save_glove_vocab_file> <save_glove_file> <save_glove_model> <save_glove_vectors>

set -e

str_time=`date +%s`

make

X_MAX=10
BINARY=2
VERBOSE=2
ALPHA=0.03
MEMORY=16
CORPUS=$1 #Corpus
MAX_ITER=20
SAVE_FILE=$3  #save file
WINDOW_SIZE=2
VOCAB_FILE=$2 #Vocab file
SAVE_MODEL=$4 #Model save
SAVE_VECTORS=$5 #Vectors save
VECTOR_SIZE=300
VOCAB_MIN_COUNT=1
NUM_THREADS=`nproc`
BUILDDIR=build
COOCCURRENCE_FILE=cooccurrence.bin
COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin

printf "$ $BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE\n"
$BUILDDIR/vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE
printf  "\n$ $BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE\n"
$BUILDDIR/cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE
printf "\n$ $BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE\n"
$BUILDDIR/shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE
printf "\n$ $BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE -alpha $ALPHA\n"
$BUILDDIR/glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE -alpha $ALPHA

printf "\n"

make clean

printf "\n"

mv *_glove.bin $4
mv *_glove.txt $5

rm -rf *.bin

end_time=`date +%s`

runtime=$( echo "$end_time - $str_time" | bc -l )

printf "# Total Training Execution Time: $runtime Seconds.\n"

exit
