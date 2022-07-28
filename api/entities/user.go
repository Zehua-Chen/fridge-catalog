package entities

type User struct {
	ID    uint64 `gorm:"primaryKey;autoIncrement"`
	Email string `gorm:"unique"`
	Name  string
}
