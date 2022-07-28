package entities

type Group struct {
	ID      uint64
	Name    string
	fridges []Fridge
}
