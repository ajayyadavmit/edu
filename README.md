# edu
New Education Framework


#### 3. **Gantt Chart**
```markdown
```mermaid
gantt
    title Project Timeline
    section Phase 1
    Task A :a1, 2023-10-01, 7d
    Task B :after a1, 5d
    section Phase 2
    Task C :2023-10-15, 5d


#### 4. **Class Diagram**
```markdown
```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +String breed
        +bark()
    }
    Animal <|-- Dog
