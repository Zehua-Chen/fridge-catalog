package entities

type Fridge struct {
	ID           uint64
	Name         string
	Compartments []Compartment
}