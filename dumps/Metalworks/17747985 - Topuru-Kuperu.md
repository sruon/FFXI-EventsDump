# 17747985 - Topuru-Kuperu

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 224 bytes            |
| Total Events     | 11                   |
| References Count | 16                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [251](#event-251)        | 0x0001       |     11 |              5 |
| [260](#event-260)        | 0x000C       |     15 |              7 |
| [261](#event-261)        | 0x001B       |     11 |              5 |
| [262](#event-262)        | 0x0026       |     11 |              5 |
| [256](#event-256)        | 0x0031       |     10 |              2 |
| [257](#event-257)        | 0x003B       |      1 |              1 |
| [65535.1](#event-655351) | 0x003C       |     12 |              3 |
| [65535.2](#event-655352) | 0x0048       |     25 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D3B      |        7483 |
|       1 | 0x1D3C      |        7484 |
|       2 | 0x1D3D      |        7485 |
|       3 | 0x1D3E      |        7486 |
|       4 | 0x1D3F      |        7487 |
|       5 | 0x6E7C      |       28284 |
|       6 | 0xA51D      |       42269 |
|       7 | 0xFFFFBFFA  |  4294950906 |
|       8 | 0x0DAE      |        3502 |
|       9 | 0x6939      |       26937 |
|      10 | 0x9D19      |       40217 |
|      11 | 0xFFFFBFE9  |  4294950889 |
|      12 | 0x06E0      |        1760 |
|      13 | 0x000D      |          13 |
|      14 | 0x6B9F      |       27551 |
|      15 | 0x9D82      |       40322 |

## String References

- **7483**: Yes, this is the Windurst consulate. Windurst...ah, fair Windurst, how I long for thee-wee...
- **7484**: A letter of introduction? You are from Windurst! Pray tell, how are things there!?
- **7485**: Oh, you want missions... Then, please speak with Consul Patt-Pott... Ah, Windurst, how I long for thee-wee...
- **7486**: You're going where all those monsters are, aren't you? I wish I was back in Windurst...it was so peaceful there.
- **7487**: You've made it back. Then you are returning to Windurst? Oh, how I envy you...

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

### Event 251

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
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7483*)
    → "Yes, this is the Windurst consulate. Windurst...ah, fair Windurst, how I long for thee-wee..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 260

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 1D 02 80  23 21 00                 ....#...#!.     
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7484*)
    → "A letter of introduction? You are from Windurst! Pray tell, how are things there!?"
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7485*)
    → "Oh, you want missions... Then, please speak with Consul Patt-Pott... Ah, Windurst, how I long for thee-wee..."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 261

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 1D 03 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7486*)
    → "You're going where all those monsters are, aren't you? I wish I was back in Windurst...it was so peaceful there."
  2: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0024 [0x21] END_EVENT
  4: 0x0025 [0x00] END_REQSTACK()
```

### Event 262

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   1E F0  FF FF 7F 1D 04 80 23 21        ........#!
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0026 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=7487*)
    → "You've made it back. Then you are returning to Windurst? Oh, how I envy you..."
  2: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002F [0x21] END_EVENT
  4: 0x0030 [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    37 05 80 06 80 07 80  08 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.284*, z=42.269*, y=-16.390*, direction=307.8°*
  1: 0x003A [0x00] END_REQSTACK()
```

### Event 257

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      22 00 37 09              ".7.
0040: 80 0A 80 0B 80 0C 80 00                           ........        
```

#### Opcodes

```
  0: 0x003C [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x003E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=26.937*, z=40.217*, y=-16.407*, direction=154.7°*
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          79 00 F8 FF FF 7F 10 D0          y.......
0050: 0E 01 32 0D 80 1F 00 0E  80 0F 80 07 80 1F 01 6F  ..2............o
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0048 [0x79] EventEntity looks at Patt-Pott (ID: 17747984/0x010ED010) (Basic look)
  1: 0x0052 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=27.551*, Z=40.322*, Y=-16.390*
  3: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0060 [0x00] END_REQSTACK()
```
