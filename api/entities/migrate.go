package entities

import (
	"gorm.io/gorm"
)

func Migrate(db *gorm.DB) error {
	var e error

	e = db.AutoMigrate(&Compartment{})

	if e != nil {
		return e
	}

	e = db.AutoMigrate(&Fridge{})

	if e != nil {
		return e
	}

	e = db.AutoMigrate(&Group{})

	if e != nil {
		return e
	}

	e = db.AutoMigrate(&User{})

	if e != nil {
		return e
	}

	return nil
}
