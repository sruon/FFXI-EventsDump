# 17498603 - Hurr the Betrayer

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 224 bytes                    |
| Total Events     | 5                            |
| References Count | 14                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [104](#event-104)     | 0x0001       |     11 |              5 |
| [105](#event-105)     | 0x000C       |     29 |             11 |
| [106](#event-106)     | 0x0029       |     25 |              9 |
| [107](#event-107)     | 0x0042       |     65 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CB2      |        7346 |
|       1 | 0x1CB3      |        7347 |
|       2 | 0x046F      |        1135 |
|       3 | 0x02ED      |         749 |
|       4 | 0x1CB5      |        7349 |
|       5 | 0x1CB4      |        7348 |
|       6 | 0x02EC      |         748 |
|       7 | 0x1CB6      |        7350 |
|       8 | 0x1CB7      |        7351 |
|       9 | 0x0055      |          85 |
|      10 | 0x00C8      |         200 |
|      11 | 0x0000      |           0 |
|      12 | 0x00B4      |         180 |
|      13 | 0x1CB8      |        7352 |

## String References

- **7346**: Whoa! Keep it down! You want me to get caught?
- **7347**: Don't go telling anyone that you saw me here. If Bou ever found me, I...
- **7348**: Whoa! Oh, it's you.
- **7349**: Bring me $0 and three $1 and I make you something nice.
- **7350**: Bring me $0 and $1 and I make you what you look for.
- **7351**: Didn't think you be back so soon. Let me get right on it...
- **7352**: Here you go, but don't tell anyone I made key for you.

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

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7346*)
    → "Whoa! Keep it down! You want me to get caught?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 29 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 00 80 23 1D 01 80  23 03 02 10 02 80 03 03  ....#...#.......
0020: 10 03 80 1D 04 80 23 21  00                       ......#!.       
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7346*)
    → "Whoa! Keep it down! You want me to get caught?"
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7347*)
    → "Don't go telling anyone that you saw me here. If Bou ever found me, I..."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x03] Work_Zone[2] = 1135*
  6: 0x001E [0x03] Work_Zone[3] = 749*
  7: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7349*)
    → "Bring me $0 and three $1 and I make you something nice."
  8: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0027 [0x21] END_EVENT
 10: 0x0028 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1E F0 FF FF 7F 1D 05           .......
0030: 80 23 03 02 10 02 80 03  03 10 06 80 1D 07 80 23  .#.............#
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7348*)
    → "Whoa! Oh, it's you."
  2: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0032 [0x03] Work_Zone[2] = 1135*
  4: 0x0037 [0x03] Work_Zone[3] = 748*
  5: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7350*)
    → "Bring me $0 and $1 and I make you what you look for."
  6: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0040 [0x21] END_EVENT
  8: 0x0041 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 65 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 20  01 42 1D 08 80 23 39 09    ..... .B...#9.
0050: 80 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .E..........fdo1
0060: 0B 80 1C 0C 80 45 0A 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0070: 66 64 69 31 0B 80 1E F0  FF FF 7F 1D 0D 80 23 20  fdi1..........# 
0080: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0049 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=7351*)
    → "Didn't think you be back so soon. Let me get right on it..."
  4: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004E [0x39] SET_ENTITY_DIRECTION(direction=0.5°*)
  6: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x0062 [0x1C] WAIT(180* ticks)
  8: 0x0065 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0076 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=7352*)
    → "Here you go, but don't tell anyone I made key for you."
 11: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x007F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0081 [0x21] END_EVENT
 14: 0x0082 [0x00] END_REQSTACK()
```
