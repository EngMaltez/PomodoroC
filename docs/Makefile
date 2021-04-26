# Makefile
TARGETS=note1.html
.PHONY: all clean see

all: $(TARGETS)

clean:
	$(RM) $(TARGETS)

see: README.html
	open $<

%.html : %.md
	pandoc -s -c ../style.css -f markdown+smart $< -o $@
