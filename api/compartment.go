package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Person struct {
	ID string `uri:"id" binding:"required"`
}

type Query struct {
	Name string `form:"name"`
}

func Compartment(context *gin.Context) {
	var person Person
	var query Query

	e := context.BindUri(&person)
	e = context.BindQuery(&query)

	if e == nil {
		context.JSON(http.StatusOK, gin.H{
			"id":   person.ID,
			"name": query.Name,
		})

		return
	}

	context.String(http.StatusInternalServerError, e.Error())
}
