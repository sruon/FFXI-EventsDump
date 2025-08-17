# 17494731 - Turbulent Storm

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 204 bytes                            |
| Total Events     | 7                                    |
| References Count | 13                                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [7](#event-7)            | 0x0001       |      1 |              1 |
| [8](#event-8)            | 0x0002       |     28 |              8 |
| [9](#event-9)            | 0x001E       |     15 |              5 |
| [16](#event-16)          | 0x002D       |     23 |              7 |
| [65535.1](#event-655351) | 0x0044       |     15 |              5 |
| [65535.2](#event-655352) | 0x0053       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x039A      |         922 |
|       1 | 0x1DD0      |        7632 |
|       2 | 0x1DD1      |        7633 |
|       3 | 0x1DD2      |        7634 |
|       4 | 0x1DCE      |        7630 |
|       5 | 0x1DCF      |        7631 |
|       6 | 0x000B      |          11 |
|       7 | 0x67AEE     |      424686 |
|       8 | 0xFFFF475E  |  4294920030 |
|       9 | 0xFFFF4480  |  4294919296 |
|      10 | 0x6723D     |      422461 |
|      11 | 0xFFFF4734  |  4294919988 |
|      12 | 0x002D      |          45 |

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

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 03  02 10 00 80 2B CB F2 0A    ..........+...
0010: 01 01 80 23 2B CB F2 0A  01 02 80 23 21 00        ...#+......#!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x03] Work_Zone[2] = 922*
  2: 0x000C [0x2B] Turbulent Storm (ID: 17494731/0x010AF2CB) [7632*]:
    → "You won't be considered a member of the Fighting Fourth until you take that $3 to Bastok and show it to Centurion Adelbrecht."
  3: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0014 [0x2B] Turbulent Storm (ID: 17494731/0x010AF2CB) [7633*]:
    → "Oh, and good luck with the entrance exam. Though, the Republic can't afford to toss away meat before putting it in the grinder, so I wouldn't worry too much about the test."
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x21] END_EVENT
  7: 0x001D [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 2B CB F2 0A 01  03 80 23 21 00           ...+......#!.   
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x2B] Turbulent Storm (ID: 17494731/0x010AF2CB) [7634*]:
    → "I heard the news, recruit. Welcome to the Fourth...but don't let it go to your head. Let's see how long you last first."
  2: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002B [0x21] END_EVENT
  4: 0x002C [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1E F0 FF               ...
0030: FF 7F 2B CB F2 0A 01 04  80 23 2B CB F2 0A 01 05  ..+......#+.....
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x2B] Turbulent Storm (ID: 17494731/0x010AF2CB) [7630*]:
    → "The roads to Bastok are crawling with ruthless beastman scouts just itching to add another notch to their axes."
  2: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003A [0x2B] Turbulent Storm (ID: 17494731/0x010AF2CB) [7631*]:
    → "If you get spotted, you can always play the brave [man/woman] and fight the scum, but the Republic needs live soldiers, not ones in body bags. Turn tail and run away, live to kill another day--that's my motto."
  4: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0042 [0x21] END_EVENT
  6: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             32 06 80 1F  00 07 80 08 80 09 80 1F      2...........
0050: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0044 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=424.686*, Z=-47.266*, Y=-48.000*
  2: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0051 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0052 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          32 06 80 1F 00  0A 80 0B 80 09 80 1F 01     2............
0060: 6F 1E F0 FF FF 7F 1C 0C  80 00                    o.........      
```

#### Opcodes

```
  0: 0x0053 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=422.461*, Z=-47.308*, Y=-48.000*
  2: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0066 [0x1C] WAIT(45* ticks)
  6: 0x0069 [0x00] END_REQSTACK()
```
