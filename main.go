package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var count uint = 1
	for _, arg := range os.Args[1:] {
		for _, w := range strings.Split(arg, " "){
			fmt.Printf("\t%d. %s\n", count, w)
			count++
		}
	}
}
