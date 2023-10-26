preprocessingTools(){
  camel_arclean |  camel_dediac | camel_word_tokenize | tr -d "[:alnum:]" | tr -d "[:punct:]"
}


echo "Preprocessing [$1] in progress ..."

cat $1 | preprocessingTools > $2
