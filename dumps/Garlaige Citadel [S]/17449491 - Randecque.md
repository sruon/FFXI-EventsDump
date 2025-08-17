# 17449491 - Randecque

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 204 bytes                      |
| Total Events     | 7                              |
| References Count | 13                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |     28 |              8 |
| [3](#event-3)            | 0x001E       |     15 |              5 |
| [12](#event-12)          | 0x002D       |     23 |              7 |
| [65535.1](#event-655351) | 0x0044       |     15 |              5 |
| [65535.2](#event-655352) | 0x0053       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0399      |         921 |
|       1 | 0x1DD6      |        7638 |
|       2 | 0x1DD7      |        7639 |
|       3 | 0x1DD8      |        7640 |
|       4 | 0x1DD4      |        7636 |
|       5 | 0x1DD5      |        7637 |
|       6 | 0x000B      |          11 |
|       7 | 0xEE69      |       61033 |
|       8 | 0x20D78     |      134520 |
|       9 | 0xFFFFE842  |  4294961218 |
|      10 | 0xEFA5      |       61349 |
|      11 | 0x218DE     |      137438 |
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

### Event 1

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

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 03  02 10 00 80 2B 13 42 0A    ..........+.B.
0010: 01 01 80 23 2B 13 42 0A  01 02 80 23 21 00        ...#+.B....#!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x03] Work_Zone[2] = 921*
  2: 0x000C [0x2B] Randecque (ID: 17449491/0x010A4213) [7638*]:
    → "Take that $3 to the San d'Orian capital and present it to Captain Mainchelite."
  3: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0014 [0x2B] Randecque (ID: 17449491/0x010A4213) [7639*]:
    → "If my memory serves me well, I seem to recall an initiation trial was required of all new recruits. Oh, but you need worry not--the assessment was nothing more than formality."
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x21] END_EVENT
  7: 0x001D [0x00] END_REQSTACK()
```

### Event 3

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
0020: FF FF 7F 2B 13 42 0A 01  03 80 23 21 00           ...+.B....#!.   
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x2B] Randecque (ID: 17449491/0x010A4213) [7640*]:
    → "Well, congratulations, recruit! I look forward to hearing the bards sing of your heroic deeds!"
  2: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002B [0x21] END_EVENT
  4: 0x002C [0x00] END_REQSTACK()
```

### Event 12

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
0030: FF 7F 2B 13 42 0A 01 04  80 23 2B 13 42 0A 01 05  ..+.B....#+.B...
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x2B] Randecque (ID: 17449491/0x010A4213) [7636*]:
    → "Take care, as the journey to the capital will not be an easy one."
  2: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003A [0x2B] Randecque (ID: 17449491/0x010A4213) [7637*]:
    → "May the divine light of the Goddess guide you."
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
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=61.033*, Z=134.520*, Y=-6.078*
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
  1: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=61.349*, Z=137.438*, Y=-6.078*
  2: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0066 [0x1C] WAIT(45* ticks)
  6: 0x0069 [0x00] END_REQSTACK()
```
