package entities

import (
	"gorm.io/gorm"
)

func Migrate(db *gorm.DB) error {
	var e error

	e = db.AutoMigrate(&User{})

	if e != nil {
		return e
	}

	return nil
}
