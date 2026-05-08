# Python Script Flow Analysis

<table>
<tr>
<td width="25%" valign="top">

## Program Flow Summary

This script is a fun LSU Tigers-themed Python program that:

1. **Starts** in the `__main__` block wrapped in a try/except
2. **Calls `get_input()`** — prompts for a name and checks if it's "ryan"
3. **Calls `get_score()`** — compares LSU vs Bama scores
4. **Calls `national_champs()`** — always prints "LSU!!!"

---

## Function Descriptions

### `get_input()`
- Prompts user for their name
- If name is "ryan" (case-insensitive, stripped), prints "GEAUX TIGERS"
- Otherwise prints "You are not Ryan"
- Returns the name

### `get_score()`
- Prompts for Bama's score and LSU's score
- Compares the two scores (note: string comparison, not integer)
- Prints a message based on which is greater

### `national_champs()`
- Prints a question about national champs
- Contains an `if True` block that always executes
- Always prints "LSU!!!"

---

## Notes

- ⚠️ **Bug**: `get_score()` compares strings, not integers. Scores should be cast with `int()`.
- The `if True` in `national_champs()` is always truthy — the else branch is unreachable.
- Exception handling catches all exceptions and prints the error message.
- Color legend:
  - 🟢 Start nodes
  - 🔴 End nodes
  - 🟡 Decision nodes
  - 🟠 Exception handling

</td>
<td width="75%" valign="top">

```mermaid
flowchart TB
    classDef startStyle fill:#90EE90,stroke:#333,stroke-width:2px,color:#000
    classDef endStyle fill:#FFB6C6,stroke:#333,stroke-width:2px,color:#000
    classDef decisionStyle fill:#FFE4B5,stroke:#333,stroke-width:2px,color:#000
    classDef exceptionStyle fill:#FFA07A,stroke:#333,stroke-width:2px,color:#000

    Start(["▶ Program Start: __main__"]):::startStyle
    TryBlock["Enter try block"]
    CallGetInput["Call get_input()"]
    CallGetScore["Call get_score()"]
    CallNationalChamps["Call national_champs()"]
    ExceptBlock["except Exception as e"]:::exceptionStyle
    PrintException["print(e)"]:::exceptionStyle
    ProgramEnd(["■ Program End"]):::endStyle

    Start --> TryBlock
    TryBlock --> CallGetInput
    CallGetInput --> GI_Entry

    subgraph get_input_sub ["get_input()"]
        direction LR
        GI_Entry([Enter]) --> GI_Prompt["name_input = input('Enter your name:')"]
        GI_Prompt --> GI_Check{"name_input.lower().strip() == 'ryan'?"}:::decisionStyle
        GI_Check -->|Yes| GI_PrintGeaux["print('GEAUX TIGERS')"]
        GI_Check -->|No| GI_PrintNot["print('You are not Ryan')"]
        GI_PrintGeaux --> GI_Return["return name_input"]
        GI_PrintNot --> GI_Return
        GI_Return --> GI_Exit([Exit])
    end

    GI_Exit --> CallGetScore
    CallGetScore --> GS_Entry

    subgraph get_score_sub ["get_score()"]
        direction LR
        GS_Entry([Enter]) --> GS_BamaInput["bama_score = input('how many points did bama score:')"]
        GS_BamaInput --> GS_LSUInput["lsu_score = input('how many points did lsu score')"]
        GS_LSUInput --> GS_Check{"lsu_score > bama_score?"}:::decisionStyle
        GS_Check -->|Yes| GS_PrintLane["print('Get on the Lane Train!')"]
        GS_Check -->|No| GS_PrintFire["print('Somebody fire this bum')"]
        GS_PrintLane --> GS_Exit([Exit])
        GS_PrintFire --> GS_Exit
    end

    GS_Exit --> CallNationalChamps
    CallNationalChamps --> NC_Entry

    subgraph national_champs_sub ["national_champs()"]
        direction LR
        NC_Entry([Enter]) --> NC_PrintQ["print('Who will be the national champs?')"]
        NC_PrintQ --> NC_Check{"if True"}:::decisionStyle
        NC_Check -->|"Always True"| NC_PrintLSU["print('LSU!!!')"]
        NC_PrintLSU --> NC_Exit([Exit])
    end

    NC_Exit --> ProgramEnd

    TryBlock -.->|"Exception raised"| ExceptBlock
    CallGetInput -.->|"Exception raised"| ExceptBlock
    CallGetScore -.->|"Exception raised"| ExceptBlock
    CallNationalChamps -.->|"Exception raised"| ExceptBlock
    ExceptBlock --> PrintException
    PrintException --> ProgramEnd
```

</td>
</tr>
</table>