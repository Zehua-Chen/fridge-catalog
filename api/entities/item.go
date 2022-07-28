package entities

import "time"

type Item struct {
	Name     string `json:"name"`
	ID       int    `gorm:"column:iid;primaryKey" json:"id"`
	Price    float32
	Amount   int
	Calories float32
	Purchase time.Time
	UseBy    time.Time `gorm:"column:use_by"`
	Level    int
	Market   string
}
