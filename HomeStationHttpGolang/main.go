package main

import (
	"encoding/json"
	"github.com/gorilla/mux"
	"log"
	"net/http"
)

// The measurement Type (more like an object)
type Measurement struct {
	ID    int     `json:"parameterId,omitempty"`
	Value float32 `json:"value,omitempty"`
}

var measure []Measurement

// create a new item
func CreateMeasurement(w http.ResponseWriter, r *http.Request) {
	//params := mux.Vars(r)
	var Measurement Measurement
	_ = json.NewDecoder(r.Body).Decode(&Measurement)
	//Measurement.ID = params["id"]
	//measure = append(measure, Measurement)
	json.NewEncoder(w).Encode(Measurement)
}

// main function to boot up everything
func main() {
	router := mux.NewRouter()
	measure = append(measure, Measurement{ID: 1, Value: 22.00})
	router.HandleFunc("/api/v1/addrecord/{id}", CreateMeasurement).Methods("POST")
  log.Println("Starting server ...")
	log.Fatal(http.ListenAndServe(":8886", router))
}
