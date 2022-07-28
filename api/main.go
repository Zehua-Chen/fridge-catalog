package main

import (
	"fmt"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/Zehua-Chen/fridge-catalog/api/server"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func main() {
	db, err := gorm.Open(sqlite.Open("database.sqlite"), &gorm.Config{})
	entities.Migrate(db)

	if err != nil {
		fmt.Println(err.Error())
		return
	} else {
		fmt.Println(db.Name())
	}

	router := server.SetupRouter(db)
	router.Run("localhost:4000")
}
