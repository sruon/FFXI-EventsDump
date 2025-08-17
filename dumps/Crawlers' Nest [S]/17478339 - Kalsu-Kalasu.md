# 17478339 - Kalsu-Kalasu

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Crawlers' Nest [S] (ID: 171) |
| Block Size       | 208 bytes                    |
| Total Events     | 7                            |
| References Count | 14                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |     28 |              8 |
| [3](#event-3)            | 0x001E       |     23 |              7 |
| [22](#event-22)          | 0x0035       |     15 |              5 |
| [65535.1](#event-655351) | 0x0044       |     15 |              5 |
| [65535.2](#event-655352) | 0x0053       |     23 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x039B      |         923 |
|       1 | 0x1DE8      |        7656 |
|       2 | 0x1DE9      |        7657 |
|       3 | 0x1DEA      |        7658 |
|       4 | 0x1DEB      |        7659 |
|       5 | 0x1DE7      |        7655 |
|       6 | 0x000B      |          11 |
|       7 | 0x4A094     |      303252 |
|       8 | 0xFFFFC0E6  |  4294951142 |
|       9 | 0xFFFF7C4A  |  4294933578 |
|      10 | 0x4A680     |      304768 |
|      11 | 0xFFFFB520  |  4294948128 |
|      12 | 0xFFFF7D11  |  4294933777 |
|      13 | 0x002D      |          45 |

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
0000:       1E F0 FF FF 7F 03  02 10 00 80 2B C3 B2 0A    ..........+...
0010: 01 01 80 23 2B C3 B2 0A  01 02 80 23 21 00        ...#+......#!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x03] Work_Zone[2] = 923*
  2: 0x000C [0x2B] Kalsu-Kalasu (ID: 17478339/0x010AB2C3) [7656*]:
    → "Don't forget to show that $3 to Cobra Lieutenant Miah Riyuh in Windurst."
  3: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0014 [0x2B] Kalsu-Kalasu (ID: 17478339/0x010AB2C3) [7657*]:
    → "A seasoned adventurer like yourself should have no problem passing the initiation!"
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x21] END_EVENT
  7: 0x001D [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 2B C3 B2 0A 01  03 80 23 2B C3 B2 0A 01  ...+......#+....
0030: 04 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x2B] Kalsu-Kalasu (ID: 17478339/0x010AB2C3) [7658*]:
    → "So, you're one of us now! Ah, victory is nigh! The Shadow Lord trembles on his throne as we speak!"
  2: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002B [0x2B] Kalsu-Kalasu (ID: 17478339/0x010AB2C3) [7659*]:
    → "And if I keep telling myself that, someday it will come true, no?"
  4: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0033 [0x21] END_EVENT
  6: 0x0034 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1E F0 FF  FF 7F 2B C3 B2 0A 01 05       .....+.....
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003A [0x2B] Kalsu-Kalasu (ID: 17478339/0x010AB2C3) [7655*]:
    → "Good luck, and may the wisdom of the stars light your path!"
  2: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0042 [0x21] END_EVENT
  4: 0x0043 [0x00] END_REQSTACK()
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
  1: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=303.252*, Z=-16.154*, Y=-33.718*
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
0050:          32 06 80 1F 00  0A 80 0B 80 0C 80 1F 01     2............
0060: 6F 1E F0 FF FF 7F 1C 0D  80 00                    o.........      
```

#### Opcodes

```
  0: 0x0053 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0056 [0x1F] MOVE_ENTITY: EventEntity moves to X=304.768*, Z=-19.168*, Y=-33.519*
  2: 0x005E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0060 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0066 [0x1C] WAIT(45* ticks)
  6: 0x0069 [0x00] END_REQSTACK()
```
