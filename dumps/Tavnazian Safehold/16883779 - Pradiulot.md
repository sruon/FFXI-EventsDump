# 16883779 - Pradiulot

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 200 bytes                   |
| Total Events     | 9                           |
| References Count | 14                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [200](#event-200)        | 0x0007       |      1 |              1 |
| [65535.1](#event-655351) | 0x0008       |      3 |              2 |
| [65535.2](#event-655352) | 0x000B       |     24 |              5 |
| [65535.3](#event-655353) | 0x0023       |     14 |              4 |
| [65535.4](#event-655354) | 0x0031       |     22 |              6 |
| [204](#event-204)        | 0x0047       |      1 |              1 |
| [65535.5](#event-655355) | 0x0048       |      6 |              3 |
| [65535.6](#event-655356) | 0x004E       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF3567  |  4294915431 |
|       2 | 0xFFFF566C  |  4294923884 |
|       3 | 0xFFFFA9DE  |  4294945246 |
|       4 | 0xFFFF4D6A  |  4294921578 |
|       5 | 0xFFFF532D  |  4294923053 |
|       6 | 0xFFFFA9E3  |  4294945251 |
|       7 | 0xFFFF588F  |  4294924431 |
|       8 | 0xFFFF58F7  |  4294924535 |
|       9 | 0xFFFFA9D3  |  4294945235 |
|      10 | 0x0867      |        2151 |
|      11 | 0xFFFED1FE  |  4294889982 |
|      12 | 0xFFFF523C  |  4294922812 |
|      13 | 0xFFFFAA10  |  4294945296 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          22 00 00                         "..     
```

#### Opcodes

```
  0: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 00 80 1F 00             2....
0010: 01 80 02 80 03 80 1F 01  79 00 43 A0 01 01 44 A0  ........y.C...D.
0020: 01 01 00                                          ...             
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.865*, Z=-43.412*, Y=-22.050*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x79] Pradiulot (ID: 16883779/0x0101A043) looks at Elysia (ID: 16883780/0x0101A044) (Basic look)
  4: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 00 80 1F 00  04 80 05 80 06 80 1F 01     2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.718*, Z=-44.243*, Y=-22.045*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 00 80 1F 00 07 80  08 80 09 80 1F 01 22 01   2............".
0040: 2F 01 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=-42.865*, Z=-42.761*, Y=-22.061*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0040 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  5: 0x0046 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          22 00 39 0A 80 00                ".9...  
```

#### Opcodes

```
  0: 0x0048 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x004A [0x39] SET_ENTITY_DIRECTION(direction=11.8°*)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            32 00                2.
0050: 80 1F 00 0B 80 0C 80 0D  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x004E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0051 [0x1F] MOVE_ENTITY: EventEntity moves to X=-77.314*, Z=-44.484*, Y=-22.000*
  2: 0x0059 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005B [0x00] END_REQSTACK()
```
