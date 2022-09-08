FROM scratch

WORKDIR /ccalc

COPY ./ccalc.elf .

CMD ["./ccalc.elf"];