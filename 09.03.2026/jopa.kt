fun main() {
    val cities = arrayOf("1 брюсель", "2 москва", "3 чернобыль", "4 крым", "5 токио лондон")
    println("вот те города")
    for (city in cities) {
        println(city)
    }
    println("напши цифру города, который хочешь изменить")
    val choice = readlnOrNull()?.toIntOrNull()
    if (choice != null && choice in 1..cities.size) {
        val index = choice - 1
        println("введи новое название города")
        val newName = readln()
        cities[index] = "$choice $newName"
        for (city in cities) {
            println(city)
        }
    } else {
        println("Ошибка: введена некорректная цифра или значение вне диапазона.")
    }
}