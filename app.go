package main

import (
    "fmt"
    "net/http"
)

func hello(w http.ResponseWriter, req *http.Request) {
    fmt.Fprintf(w, "Hello Go World!\n")
}

func main() {
    http.HandleFunc("/hello", hello)
    http.ListenAndServe(":3000", nil)
}
