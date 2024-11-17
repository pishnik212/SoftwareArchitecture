## 

## 1.	Диаграмма системного контекста

 <img width="300" src="Images/1.svg" alt="1"/>

Код:

```messagebus
@startuml


!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

' uncomment the following line and comment the first to use locally

' !include C4_Container.puml



AddElementTag("microService", $shape=EightSidedShape(), $bgColor="CornflowerBlue", $fontColor="white", $legendText="micro service\neight sided")

AddElementTag("storage", $shape=RoundedBoxShape(), $bgColor="lightSkyBlue", $fontColor="white")



SHOW_PERSON_OUTLINE()



Person(admin, Администратор)

Person(admissionsOfficer, Сотрудник приемной комиссии)

Container(c1, "Система анализа списка абитуриентов", "System")

Container(c2, "Модель машинного обучения с предсказанием балла зеленой волны", "Model")



Rel(admin, c1, "Загружает списки абитуриентов")

Rel_D(admissionsOfficer, c1, "Получает списки и взаимодействует с ними")

Rel_D(c1, c2, "Передает загруженные данные")

Rel_D(c2, c1, "Передаёт предсказанные значения")



SHOW_LEGEND()

@enduml
```
