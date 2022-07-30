package entities

type Group struct {
	ID      uint64    `json:"id"`
	Name    string    `json:"name"`
	Fridges []*Fridge `json:"fridges" gorm:"many2many:groups_fridges"`
	Users   []*User   `json:"users" gorm:"many2many:groups_users"`
}
