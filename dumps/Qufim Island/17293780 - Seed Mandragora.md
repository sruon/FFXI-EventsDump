# 17293780 - Seed Mandragora

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 264 bytes              |
| Total Events     | 13                     |
| References Count | 19                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      4 |              2 |
| [65535.1](#event-655351) | 0x0005       |      5 |              2 |
| [65535.2](#event-655352) | 0x000A       |     20 |              5 |
| [65535.3](#event-655353) | 0x001E       |     20 |              5 |
| [65535.4](#event-655354) | 0x0032       |      5 |              2 |
| [65535.5](#event-655355) | 0x0037       |      5 |              2 |
| [65535.6](#event-655356) | 0x003C       |      5 |              2 |
| [65535.7](#event-655357) | 0x0041       |      5 |              2 |
| [32](#event-32)          | 0x0046       |      4 |              2 |
| [65535.8](#event-655358) | 0x004A       |     20 |              5 |
| [65535.9](#event-655359) | 0x005E       |     20 |              5 |
| [34](#event-34)          | 0x0072       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x092F      |        2351 |
|       2 | 0x000D      |          13 |
|       3 | 0x8FE6      |       36838 |
|       4 | 0x41D0F     |      269583 |
|       5 | 0xFFFFB253  |  4294947411 |
|       6 | 0xFFFECB86  |  4294888326 |
|       7 | 0x4FA2E     |      326190 |
|       8 | 0xFFFF61F4  |  4294926836 |
|       9 | 0x0164      |         356 |
|      10 | 0x0025      |          37 |
|      11 | 0x012C      |         300 |
|      12 | 0x0930      |        2352 |
|      13 | 0xFFFE0B48  |  4294839112 |
|      14 | 0x47C5F     |      293983 |
|      15 | 0xFFFFB3E3  |  4294947811 |
|      16 | 0x0028      |          40 |
|      17 | 0xFFFE1958  |  4294842712 |
|      18 | 0x48817     |      296983 |

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

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C0 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                B6 00 01  80 00                         .....      
```

#### Opcodes

```
  0: 0x0005 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2351*)
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000A   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                59 04 D4 E1 07 01            Y.....
0010: 02 80 1F 00 03 80 04 80  05 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x000A [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293780/0x0107E1D4) main speed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=36.838*, Z=269.583*, Y=-19.885*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            59 04                Y.
0020: D4 E1 07 01 02 80 1F 00  06 80 07 80 08 80 1F 01  ................
0030: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x001E [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293780/0x0107E1D4) main speed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-78.970*, Z=326.190*, Y=-40.460*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       B6 00 09 80 00                                .....         
```

#### Opcodes

```
  0: 0x0032 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=356*)
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      B6  00 0A 80 00                     .....    
```

#### Opcodes

```
  0: 0x0037 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=37*)
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      B6 00 0B 80              ....
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x003C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=300*)
  1: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    B6 00 0C 80 00                                  .....          
```

#### Opcodes

```
  0: 0x0041 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2352*)
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   C0 00  80 00                          ....      
```

#### Opcodes

```
  0: 0x0046 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                59 04 D4 E1 07 01            Y.....
0050: 02 80 1F 00 0D 80 0E 80  0F 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x004A [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293780/0x0107E1D4) main speed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-128.184*, Z=293.983*, Y=-19.485*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            59 04                Y.
0060: D4 E1 07 01 10 80 1F 00  11 80 12 80 0F 80 1F 01  ................
0070: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x005E [0x59] UPDATE_ENTITY_DATA: Set Seed Mandragora (ID: 17293780/0x0107E1D4) main speed = 40* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=-124.584*, Z=296.983*, Y=-19.485*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0071 [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0072  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       C0 00 80 00                                   ....          
```

#### Opcodes

```
  0: 0x0072 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0075 [0x00] END_REQSTACK()
```
