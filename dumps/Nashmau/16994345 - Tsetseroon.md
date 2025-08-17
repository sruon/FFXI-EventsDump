# 16994345 - Tsetseroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 288 bytes        |
| Total Events     | 12               |
| References Count | 19               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |      1 |              1 |
| [17](#event-17)          | 0x0002       |     27 |             11 |
| [18](#event-18)          | 0x001D       |      1 |              1 |
| [19](#event-19)          | 0x001E       |     13 |              7 |
| [20](#event-20)          | 0x002B       |      1 |              1 |
| [21](#event-21)          | 0x002C       |     13 |              7 |
| [4](#event-4)            | 0x0039       |     13 |              7 |
| [65535.1](#event-655351) | 0x0046       |     19 |              3 |
| [294](#event-294)        | 0x0059       |     10 |              2 |
| [65535.2](#event-655352) | 0x0063       |     33 |              7 |
| [65535.3](#event-655353) | 0x0084       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x291C      |       10524 |
|       1 | 0x115B      |        4443 |
|       2 | 0x0281      |         641 |
|       3 | 0x291D      |       10525 |
|       4 | 0x2925      |       10533 |
|       5 | 0x292A      |       10538 |
|       6 | 0x2909      |       10505 |
|       7 | 0x0078      |         120 |
|       8 | 0x034B      |         843 |
|       9 | 0x6970      |       26992 |
|      10 | 0xEFDE      |       61406 |
|      11 | 0xFFFFE891  |  4294961297 |
|      12 | 0x0FFF      |        4095 |
|      13 | 0x000A      |          10 |
|      14 | 0x5A14      |       23060 |
|      15 | 0x10607     |       67079 |
|      16 | 0x000F      |          15 |
|      17 | 0x034A      |         842 |
|      18 | 0x0028      |          40 |

## String References

- **10505**: Tsetseroon so looonely.
- **10524**: Tsetseroon block his "Treasooor Huntooor" with special stooo!
- **10525**: But Tsetseroon need $0 and $1 tooo make it, yes?
- **10533**: Yooo bring stooo to place that smell like Wawaroon? If yooo wooodn't mind?
- **10538**: Yooo toook down Wawaroon? Wawaroon is dooown? Treasooor Huntooor, bye bye? Ooo...soooper soooper! Tsetseroon happy!

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

### Event 16

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

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 27 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 1D 00 80 23 03 02 10    .....op...#...
0010: 01 80 03 03 10 02 80 1D  03 80 23 21 00           ..........#!.   
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=10524*)
    → "Tsetseroon block his "Treasooor Huntooor" with special stooo!"
  4: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000D [0x03] Work_Zone[2] = 4443*
  6: 0x0012 [0x03] Work_Zone[3] = 641*
  7: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10525*)
    → "But Tsetseroon need $0 and $1 tooo make it, yes?"
  8: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x001B [0x21] END_EVENT
 10: 0x001C [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1E F0                ..
0020: FF FF 7F 6F 70 1D 04 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x001E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0023 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0024 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=10533*)
    → "Yooo bring stooo to place that smell like Wawaroon? If yooo wooodn't mind?"
  4: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0029 [0x21] END_EVENT
  6: 0x002A [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   00                         .    
```

#### Opcodes

```
  0: 0x002B [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      1E F0 FF FF              ....
0030: 7F 6F 70 1D 05 80 23 21  00                       .op...#!.       
```

#### Opcodes

```
  0: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0032 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=10538*)
    → "Yooo toook down Wawaroon? Wawaroon is dooown? Treasooor Huntooor, bye bye? Ooo...soooper soooper! Tsetseroon happy!"
  4: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0037 [0x21] END_EVENT
  6: 0x0038 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1E F0 FF FF 7F 6F 70           .....op
0040: 1D 06 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0040 [0x1D] PRINT_EVENT_MESSAGE(message_id=10505*)
    → "Tsetseroon so looonely."
  4: 0x0043 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0044 [0x21] END_EVENT
  6: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   1C 07  80 5B 08 80 29 50 03 01        ...[..)P..
0050: 29 50 03 01 74 6C 62 30  00                       )P..tlb0.       
```

#### Opcodes

```
  0: 0x0046 [0x1C] WAIT(120* ticks)
  1: 0x0049 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Tsetseroon (ID: 16994345/0x01035029), Tsetseroon (ID: 16994345/0x01035029)], work=843*
  2: 0x0058 [0x00] END_REQSTACK()
```

### Event 294

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             37 09 80 0A 80 0B 80           7......
0060: 0C 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0059 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.992*, z=61.406*, y=-5.999*, direction=359.9°*
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          32 0D 80 1F 00  0E 80 0F 80 0B 80 1F 01     2............
0070: 6F 1C 10 80 5B 11 80 29  50 03 01 29 50 03 01 74  o...[..)P..)P..t
0080: 68 6B 30 00                                       hk0.            
```

#### Opcodes

```
  0: 0x0063 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=23.060*, Z=67.079*, Y=-5.999*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0071 [0x1C] WAIT(15* ticks)
  5: 0x0074 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [Tsetseroon (ID: 16994345/0x01035029), Tsetseroon (ID: 16994345/0x01035029)], work=842*
  6: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             32 12 80 1F  00 09 80 0A 80 0B 80 1F      2...........
0090: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0084 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0087 [0x1F] MOVE_ENTITY: EventEntity moves to X=26.992*, Z=61.406*, Y=-5.999*
  2: 0x008F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0091 [0x00] END_REQSTACK()
```
