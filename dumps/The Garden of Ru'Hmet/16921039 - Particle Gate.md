# 16921039 - Particle Gate

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | The Garden of Ru'Hmet (ID: 35) |
| Block Size       | 332 bytes                      |
| Total Events     | 7                              |
| References Count | 11                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [112](#event-112)        | 0x0001       |    177 |             41 |
| [203](#event-203)        | 0x00B2       |      1 |              1 |
| [32000](#event-32000)    | 0x00B3       |      1 |              1 |
| [65535.1](#event-655351) | 0x00B4       |     18 |              4 |
| [65535.2](#event-655352) | 0x00C6       |     31 |              5 |
| [65535.3](#event-655353) | 0x00E5       |     15 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DD2      |        7634 |
|       1 | 0x1D21      |        7457 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D22      |        7458 |
|       4 | 0x0001      |           1 |
|       5 | 0x1D23      |        7459 |
|       6 | 0x668B4     |      420020 |
|       7 | 0x5F59D     |      390557 |
|       8 | 0x0400      |        1024 |
|       9 | 0x0002      |           2 |
|      10 | 0x012C      |         300 |

## String References

- **7457**: Choose your path... [Leave the Garden of Ru'Hmet./Return to the room entrance./Nothing.]
- **7458**: Return to the grand palace? [Yes./No.]
- **7459**: Return to the chamber entrance? [Yes./No.]
- **7634**: You feel a mysterious energy emanating from the glowing stone in the center of the portal.

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

### Event 112

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 177 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 4C 00 24 03 80  04 80 02 80 25 02 00 10  ...L.$......%...
0020: 02 80 00 39 00 42 43 00  43 01 03 01 10 04 80 29  ...9.BC.C......)
0030: 01 F0 FF FF 7F 15 01 49  00 02 00 10 04 80 00 49  .......I.......I
0040: 00 03 01 10 02 80 01 49  00 01 AE 00 02 00 10 04  .......I........
0050: 80 00 9E 00 24 05 80 04  80 02 80 25 02 00 10 02  ....$......%....
0060: 80 00 8B 00 42 43 00 43  01 03 01 10 02 80 29 01  ....BC.C......).
0070: F0 FF FF 7F 15 47 00 06  80 07 80 02 80 08 80 47  .....G.........G
0080: 01 29 01 F0 FF FF 7F 16  01 9B 00 02 00 10 04 80  .)..............
0090: 00 9B 00 03 01 10 02 80  01 9B 00 01 AE 00 02 00  ................
00A0: 10 09 80 00 AE 00 03 01  10 02 80 01 AE 00 20 00  .............. .
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7634*]:
    → "You feel a mysterious energy emanating from the glowing stone in the center of the portal."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7457*, default_option=0*, option_flags=0*)
    → "Choose your path... [Leave the Garden of Ru'Hmet./Return to the room entrance./Nothing.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004C
  5: 0x0015 [0x24] CREATE_DIALOG(message_id=7458*, default_option=1*, option_flags=0*)
    → "Return to the grand palace? [Yes./No.]"
  6: 0x001C [0x25] WAIT_DIALOG_SELECT()
  7: 0x001D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0039
  8: 0x0025 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0026 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0028 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x002A [0x03] Work_Zone[1] = 1*
 12: 0x002F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x15)
 13: 0x0036 [0x01] GOTO 0x0049
 14: 0x0039 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0049
 15: 0x0041 [0x03] Work_Zone[1] = 0*
 16: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 17: 0x0049 [0x01] GOTO 0x00AE
 18: 0x004C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x009E
 19: 0x0054 [0x24] CREATE_DIALOG(message_id=7459*, default_option=1*, option_flags=0*)
    → "Return to the chamber entrance? [Yes./No.]"
 20: 0x005B [0x25] WAIT_DIALOG_SELECT()
 21: 0x005C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008B
 22: 0x0064 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 23: 0x0065 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 24: 0x0067 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 25: 0x0069 [0x03] Work_Zone[1] = 0*
 26: 0x006E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x15)
 27: 0x0075 [0x47] UPDATE_PLAYER_POS(420.020*, 390.557*, 0.000*, yaw=90.0°*)
 28: 0x007F [0x47] WAIT_PLAYER_POS_UPDATE
 29: 0x0081 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x16)
 30: 0x0088 [0x01] GOTO 0x009B
 31: 0x008B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x009B
 32: 0x0093 [0x03] Work_Zone[1] = 0*
 33: 0x0098 [0x01] GOTO 0x009B

SUBROUTINE_009B:
 34: 0x009B [0x01] GOTO 0x00AE
 35: 0x009E [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00AE
 36: 0x00A6 [0x03] Work_Zone[1] = 0*
 37: 0x00AB [0x01] GOTO 0x00AE

SUBROUTINE_00AE:
 38: 0x00AE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 39: 0x00B0 [0x21] END_EVENT
 40: 0x00B1 [0x00] END_REQSTACK()
```

### Event 203

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       00                                            .             
```

#### Opcodes

```
  0: 0x00B2 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          00                                          .            
```

#### Opcodes

```
  0: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             4C 2D F8 FF  FF 7F F8 FF FF 7F 65 6E      L-........en
00C0: 64 31 1C 0A 80 00                                 d1....          
```

#### Opcodes

```
  0: 0x00B4 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00B5 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "end1" with entities [EventEntity, EventEntity]
  2: 0x00C2 [0x1C] WAIT(300* ticks)
  3: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 31 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   4D 2D  F8 FF FF 7F F8 FF FF 7F        M-........
00D0: 64 6F 72 31 2D F8 FF FF  7F F8 FF FF 7F 6C 6F 70  dor1-........lop
00E0: 31 1C 0A 80 00                                    1....           
```

#### Opcodes

```
  0: 0x00C6 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x00C7 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "dor1" with entities [EventEntity, EventEntity]
  2: 0x00D4 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "lop1" with entities [EventEntity, EventEntity]
  3: 0x00E1 [0x1C] WAIT(300* ticks)
  4: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                4C 2D F8  FF FF 7F F8 FF FF 7F 65       L-........e
00F0: 6E 64 31 00                                       nd1.            
```

#### Opcodes

```
  0: 0x00E5 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x00E6 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "end1" with entities [EventEntity, EventEntity]
  2: 0x00F3 [0x00] END_REQSTACK()
```
