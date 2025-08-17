# 17637397 - Promathia BattleField

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 148 bytes         |
| Total Events     | 2                 |
| References Count | 7                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [45](#event-45)       | 0x0001       |     95 |             21 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C17      |        7191 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x1C18      |        7192 |
|       4 | 0x0002      |           2 |
|       5 | 0x1C19      |        7193 |
|       6 | 0x0064      |         100 |

## String References

- **7191**: Do what? [Nothing./Set BF flag./Cancel 5 day wait period.]
- **7192**: [Quit./Holla ENM flag./Dem ENM flag./Mea ENM flag./Vahzl ENM flag./Monarch Linn ENM flag./Shrouded Maw ENM flag./Mine 2716 ENM flag./Bearclaw ENM flag./Boneyard ENM flag./Mine 2716 Mannequin ENM flag.]
- **7193**: [Quit./BF wait all off./Holla BF wait off./Dem BF wait off./Mea BF wait off./Vahzl BF wait off./Monarch Linn BF wait off./Shrouded Maw BF wait off./Mine 2716 BF wait off./Bearclaw BF wait off./Boneyard BF wait off./Mine 2716 Mannequin BF wait off.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 95 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 02 80 00 31   $......%......1
0010: 00 24 03 80 01 80 01 80  25 02 00 10 01 80 00 29  .$......%......)
0020: 00 03 01 10 00 10 01 2E  00 03 01 10 00 10 01 5E  ...............^
0030: 00 02 00 10 04 80 00 5E  00 24 05 80 01 80 01 80  .......^.$......
0040: 25 02 00 10 01 80 00 51  00 03 01 10 00 10 01 5B  %......Q.......[
0050: 00 03 01 10 00 10 07 01  10 06 80 01 5E 00 21 00  ............^.!.
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7191*, default_option=0*, option_flags=0*)
    → "Do what? [Nothing./Set BF flag./Cancel 5 day wait period.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0031
  3: 0x0011 [0x24] CREATE_DIALOG(message_id=7192*, default_option=0*, option_flags=0*)
    → "[Quit./Holla ENM flag./Dem ENM flag./Mea ENM flag./Vahzl ENM flag./Monarch Linn ENM flag./Shrouded Maw ENM flag./Mine 2716 ENM flag./Bearclaw ENM flag./Boneyard ENM flag./Mine 2716 Mannequin ENM flag.]"
  4: 0x0018 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = Work_Zone[0]
  7: 0x0026 [0x01] GOTO 0x002E
  8: 0x0029 [0x03] Work_Zone[1] = Work_Zone[0]

SUBROUTINE_002E:
  9: 0x002E [0x01] GOTO 0x005E
 10: 0x0031 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x005E
 11: 0x0039 [0x24] CREATE_DIALOG(message_id=7193*, default_option=0*, option_flags=0*)
    → "[Quit./BF wait all off./Holla BF wait off./Dem BF wait off./Mea BF wait off./Vahzl BF wait off./Monarch Linn BF wait off./Shrouded Maw BF wait off./Mine 2716 BF wait off./Bearclaw BF wait off./Boneyard BF wait off./Mine 2716 Mannequin BF wait off.]"
 12: 0x0040 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0041 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0051
 14: 0x0049 [0x03] Work_Zone[1] = Work_Zone[0]
 15: 0x004E [0x01] GOTO 0x005B
 16: 0x0051 [0x03] Work_Zone[1] = Work_Zone[0]
 17: 0x0056 [0x07] Work_Zone[1] += 100*

SUBROUTINE_005B:
 18: 0x005B [0x01] GOTO 0x005E

SUBROUTINE_005E:
 19: 0x005E [0x21] END_EVENT
 20: 0x005F [0x00] END_REQSTACK()
```
