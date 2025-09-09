Feature: Calculator

  Scenario Outline: Calculator function of 2 given numbers
    Given first number as <a> and Second Number as <b>
    When operation <Operation> is performed
    Then Result should match <Result>

    Examples:
      | a  | b  | Operation | Result |
      | 10 | 20 | Add       |     30 |
      | 20 | 20 | Sub       |      0 |
      |  4 |  8 | Mul       |     32 |
      | 40 | 20 | Div       |      2 |
