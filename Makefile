# Makefile
TARGETS=README.html
.PHONY: all clean see

all: $(TARGETS)

clean:
	$(RM) $(TARGETS)

see: README.html
	open $<

%.html : %.md
	pandoc -s -c pandoc.css -f markdown+smart $< -o $@
