# 17412783 - Five Moons

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Castle Zvahl Keep [S] (ID: 155) |
| Block Size       | 368 bytes                       |
| Total Events     | 12                              |
| References Count | 25                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      7 |              2 |
| [17](#event-17)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     22 |              6 |
| [65535.2](#event-655352) | 0x0025       |     13 |              3 |
| [18](#event-18)          | 0x0032       |      7 |              2 |
| [65535.3](#event-655353) | 0x0039       |     19 |              5 |
| [65535.4](#event-655354) | 0x004C       |     30 |              7 |
| [65535.5](#event-655355) | 0x006A       |     19 |              5 |
| [65535.6](#event-655356) | 0x007D       |     19 |              5 |
| [65535.7](#event-655357) | 0x0090       |     27 |              7 |
| [65535.8](#event-655358) | 0x00AB       |     33 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFA3EAA  |  4294590122 |
|       2 | 0xFFFE7161  |  4294865249 |
|       3 | 0xFFFF34E0  |  4294915296 |
|       4 | 0x001E      |          30 |
|       5 | 0x0019      |          25 |
|       6 | 0xFFFA6F3F  |  4294602559 |
|       7 | 0xFFFE72EA  |  4294865642 |
|       8 | 0xFFFF34E1  |  4294915297 |
|       9 | 0x003C      |          60 |
|      10 | 0x00B4      |         180 |
|      11 | 0x000D      |          13 |
|      12 | 0xFFFA6AC6  |  4294601414 |
|      13 | 0xFFFE8E08  |  4294872584 |
|      14 | 0xFFFA2400  |  4294583296 |
|      15 | 0xFFFE89C8  |  4294871496 |
|      16 | 0xFFFA521E  |  4294595102 |
|      17 | 0xFFFE6C57  |  4294863959 |
|      18 | 0x005A      |          90 |
|      19 | 0xFFFA4CA9  |  4294593705 |
|      20 | 0xFFFE6769  |  4294862697 |
|      21 | 0xFFFA562C  |  4294596140 |
|      22 | 0xFFFE6194  |  4294861204 |
|      23 | 0xFFFA82FB  |  4294607611 |
|      24 | 0xFFFE64B4  |  4294862004 |

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

### Event 15

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1E B7 B2 09  ................
0020: 01 1C 04 80 00                                    .....           
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=-377.174*, Z=-102.047*, Y=-52.000*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1E] EventEntity looks at Marquis Amon (ID: 17412791/0x0109B2B7) and starts talking
  4: 0x0021 [0x1C] WAIT(30* ticks)
  5: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                6E AF B2  09 01 05 80 99 AF B2 09       n..........
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0025 [0x6E] Five Moons (ID: 17412783/0x0109B2AF) uses emote 25*
  1: 0x002C [0x99] Wait for Five Moons (ID: 17412783/0x0109B2AF) animation to complete
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0032 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 06 80           2......
0040: 07 80 08 80 1F 01 1E F0  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-364.737*, Z=-101.654*, Y=-51.999*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      1C 09 80 79              ...y
0050: 00 AF B2 09 01 C1 B2 09  01 1C 0A 80 32 0B 80 1F  ............2...
0060: 00 0C 80 0D 80 08 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x004C [0x1C] WAIT(60* ticks)
  1: 0x004F [0x79] Five Moons (ID: 17412783/0x0109B2AF) looks at noname (ID: 17412801/0x0109B2C1) (Basic look)
  2: 0x0059 [0x1C] WAIT(180* ticks)
  3: 0x005C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=-365.882*, Z=-94.712*, Y=-51.999*
  5: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                32 0B 80 1F 00 0E            2.....
0070: 80 0F 80 08 80 1F 01 1E  C1 B2 09 01 00           .............   
```

#### Opcodes

```
  0: 0x006A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=-384.000*, Z=-95.800*, Y=-51.999*
  2: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0077 [0x1E] EventEntity looks at noname (ID: 17412801/0x0109B2C1) and starts talking
  4: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         32 00 80               2..
0080: 1F 00 10 80 11 80 08 80  1F 01 1E F0 FF FF 7F 00  ................
```

#### Opcodes

```
  0: 0x007D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0080 [0x1F] MOVE_ENTITY: EventEntity moves to X=-372.194*, Z=-103.337*, Y=-51.999*
  2: 0x0088 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x008A [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x008F [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 1E B3 B2 09 01 1C 12 80  32 0B 80 1F 00 13 80 14  ........2.......
00A0: 80 08 80 1F 01 1E B3 B2  09 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0090 [0x1E] EventEntity looks at Allenberge (ID: 17412787/0x0109B2B3) and starts talking
  1: 0x0095 [0x1C] WAIT(90* ticks)
  2: 0x0098 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x009B [0x1F] MOVE_ENTITY: EventEntity moves to X=-373.591*, Z=-104.599*, Y=-51.999*
  4: 0x00A3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00A5 [0x1E] EventEntity looks at Allenberge (ID: 17412787/0x0109B2B3) and starts talking
  6: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   32 00 80 1F 00             2....
00B0: 15 80 16 80 08 80 1F 01  4A B3 B2 09 01 AC B2 09  ........J.......
00C0: 01 1F 00 17 80 18 80 08  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x00AB [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-371.156*, Z=-106.092*, Y=-51.999*
  2: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B8 [0x4A] Allenberge (ID: 17412787/0x0109B2B3) looks at Volker (ID: 17412780/0x0109B2AC)
  4: 0x00C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-359.685*, Z=-105.292*, Y=-51.999*
  5: 0x00C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00CB [0x00] END_REQSTACK()
```
