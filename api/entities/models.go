package entities

import (
	"time"

	"gorm.io/gorm"
)

type Compartment struct {
	Level       int     `gorm:"column:clevel;primaryKey" json:"level"`
	Temperature float32 `json:"temperature"`
}

type User struct {
	ID    uint64 `gorm:"primaryKey;autoIncrement"`
	Email string `gorm:"unique"`
	Name  string
}

type Market struct {
	Name     string `gorm:"column:mname;primaryKey" json:"name"`
	Location string `json:"location"`
}

type Nutrient struct {
	Name string `gorm:"column:nname;primaryKey" json:"name"`
}

type PreparationMethod struct {
	Name string `gorm:"column:method;primaryKey" json:"name"`
}

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

func Migrate(db *gorm.DB) error {
	var e error

	e = db.AutoMigrate(&User{})

	if e != nil {
		return e
	}

	return nil
}
