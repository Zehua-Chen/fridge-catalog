package entities

type Compartment struct {
	Level       int     `gorm:"column:clevel;primaryKey" json:"level"`
	Temperature float32 `json:"temperature"`
}
