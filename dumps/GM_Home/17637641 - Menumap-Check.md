# 17637641 - Menumap-Check

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 132 bytes         |
| Total Events     | 2                 |
| References Count | 6                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [201](#event-201)     | 0x0001       |     80 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x2423      |        9251 |
|       2 | 0x0001      |           1 |
|       3 | 0x2424      |        9252 |
|       4 | 0x01F4      |         500 |
|       5 | 0x0258      |         600 |

## String References

- **9251**: Check which map number? [True value./False value.]
- **9252**: Do not include hyphens in the False value.

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

### Event 201

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 80 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 24 01  80 00 80 00 80 25 02 00   .....$......%..
0010: 10 00 80 00 21 00 71 10  02 80 71 11 00 00 01 3C  ....!.q...q....<
0020: 00 02 00 10 02 80 00 3C  00 48 03 80 71 10 02 80  .......<.H..q...
0030: 71 11 02 10 08 00 00 02  10 01 3C 00 89 00 00 B4  q.........<.....
0040: 14 00 80 00 80 04 80 00  80 02 80 1C 05 80 8A 21  ...............!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=9251*, default_option=0*, option_flags=0*)
    → "Check which map number? [True value./False value.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0021
  4: 0x0016 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  5: 0x001A [0x71] USER_INPUT_HANDLER: Process numerical input A (work=ExtData[1]->WorkLocal[0])
  6: 0x001E [0x01] GOTO 0x003C
  7: 0x0021 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x003C
  8: 0x0029 [0x48] [System] [9252*]:
    → "Do not include hyphens in the False value."
  9: 0x002C [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
 10: 0x0030 [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[2])
 11: 0x0034 [0x08] ExtData[1]->WorkLocal[0] -= Work_Zone[2]
 12: 0x0039 [0x01] GOTO 0x003C

SUBROUTINE_003C:
 13: 0x003C [0x89] OPEN_MAP(map_id=0x00000000)
 14: 0x003F [0xB4] UI_WINDOW_STRING_HANDLER(case=0x14 - Update map window values, work_offset1=0*, work_offset2=0*, work_offset3=500*, work_offset4=0*, work_offset5=1*)
 15: 0x004B [0x1C] WAIT(600* ticks)
 16: 0x004E [0x8A] CLOSE_MAP()
 17: 0x004F [0x21] END_EVENT
 18: 0x0050 [0x00] END_REQSTACK()
```
