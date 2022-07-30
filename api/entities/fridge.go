package entities

type Fridge struct {
	ID           uint64         `json:"id"`
	Name         string         `json:"name"`
	Compartments []*Compartment `gorm:"many2many:fridges_compartments"`
}
