CC = gcc
#For older gcc, use -O3 or -O2 instead of -Ofast
# CFLAGS = -lm -pthread -Ofast -march=native -funroll-loops -Wno-unused-result #for all machines
CFLAGS = -lm -pthread -Ofast -mcpu=apple-a14 -funroll-loops -Wall -Wextra -Wpedantic -w #only for MacBook Pro 14 m1 chips
BUILDDIR := build
SRCDIR := src

all: dir glove shuffle cooccur vocab_count

dir :
		mkdir -p $(BUILDDIR)

glove : $(SRCDIR)/glove.c
		$(CC) $(SRCDIR)/glove.c -o $(BUILDDIR)/glove $(CFLAGS)

shuffle : $(SRCDIR)/shuffle.c
		$(CC) $(SRCDIR)/shuffle.c -o $(BUILDDIR)/shuffle $(CFLAGS)

cooccur : $(SRCDIR)/cooccur.c
		$(CC) $(SRCDIR)/cooccur.c -o $(BUILDDIR)/cooccur $(CFLAGS)

vocab_count : $(SRCDIR)/vocab_count.c
		$(CC) $(SRCDIR)/vocab_count.c -o $(BUILDDIR)/vocab_count $(CFLAGS)

clean:
		rm -rf glove shuffle cooccur vocab_count build
