# 16982471 - Rongelouts

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 236 bytes                     |
| Total Events     | 16                            |
| References Count | 12                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [5071](#event-5071)       | 0x0001       |      1 |              1 |
| [5073](#event-5073)       | 0x0002       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0003       |     47 |              8 |
| [65535.2](#event-65535-2) | 0x0032       |     47 |              8 |
| [5075](#event-5075)       | 0x0061       |      1 |              1 |
| [5076](#event-5076)       | 0x0062       |      1 |              1 |
| [5077](#event-5077)       | 0x0063       |      1 |              1 |
| [5078](#event-5078)       | 0x0064       |      1 |              1 |
| [5080](#event-5080)       | 0x0065       |      1 |              1 |
| [5081](#event-5081)       | 0x0066       |      1 |              1 |
| [5082](#event-5082)       | 0x0067       |      1 |              1 |
| [5083](#event-5083)       | 0x0068       |      1 |              1 |
| [5084](#event-5084)       | 0x0069       |      1 |              1 |
| [5085](#event-5085)       | 0x006A       |      1 |              1 |
| [5086](#event-5086)       | 0x006B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF75B69  |  4294400873 |
|       1 | 0xA409      |       41993 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x07D0      |        2000 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFF75CF7  |  4294401271 |
|       6 | 0x9287      |       37511 |
|       7 | 0xFFF75C8B  |  4294401163 |
|       8 | 0x94F4      |       38132 |
|       9 | 0x050C      |        1292 |
|      10 | 0xFFF75D51  |  4294401361 |
|      11 | 0xA6B9      |       42681 |

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

### Event 5071

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

### Event 5073

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 47 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          BA C7 21 03 01  00 80 01 80 02 80 03 80     ..!..........
0010: 32 04 80 79 00 C7 21 03  01 D3 20 03 01 1F 00 05  2..y..!... .....
0020: 80 06 80 02 80 1F 01 6F  4A C7 21 03 01 D3 20 03  .......oJ.!... .
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0003 [0xBA] SET_ENTITY_POSITION(entity_id=Rongelouts (ID: 16982471/0x010321C7), pos_x=-566.423*, pos_z=41.993*, pos_y=1.999*, direction=175.8°*)
  1: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0013 [0x79] Rongelouts (ID: 16982471/0x010321C7) looks at Falzum (ID: 16982227/0x010320D3) (Basic look)
  3: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-566.025*, Z=37.511*, Y=1.999*
  4: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0028 [0x4A] Rongelouts (ID: 16982471/0x010321C7) looks at Falzum (ID: 16982227/0x010320D3)
  7: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 47 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       BA C7 21 03 01 07  80 08 80 02 80 09 80 32    ..!..........2
0040: 04 80 79 00 C7 21 03 01  CB 21 03 01 1F 00 0A 80  ..y..!...!......
0050: 0B 80 02 80 1F 01 6F 4A  C7 21 03 01 CB 21 03 01  ......oJ.!...!..
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x0032 [0xBA] SET_ENTITY_POSITION(entity_id=Rongelouts (ID: 16982471/0x010321C7), pos_x=-566.133*, pos_z=38.132*, pos_y=1.999*, direction=113.6°*)
  1: 0x003F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0042 [0x79] Rongelouts (ID: 16982471/0x010321C7) looks at Neosaliat (ID: 16982475/0x010321CB) (Basic look)
  3: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-565.935*, Z=42.681*, Y=1.999*
  4: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0057 [0x4A] Rongelouts (ID: 16982471/0x010321C7) looks at Neosaliat (ID: 16982475/0x010321CB)
  7: 0x0060 [0x00] END_REQSTACK()
```

### Event 5075

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0061  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    00                                              .              
```

#### Opcodes

```
  0: 0x0061 [0x00] END_REQSTACK()
```

### Event 5076

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0062  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       00                                            .             
```

#### Opcodes

```
  0: 0x0062 [0x00] END_REQSTACK()
```

### Event 5077

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 5078

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```

### Event 5080

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0065  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                00                                      .          
```

#### Opcodes

```
  0: 0x0065 [0x00] END_REQSTACK()
```

### Event 5081

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   00                                    .         
```

#### Opcodes

```
  0: 0x0066 [0x00] END_REQSTACK()
```

### Event 5082

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      00                                  .        
```

#### Opcodes

```
  0: 0x0067 [0x00] END_REQSTACK()
```

### Event 5083

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0068  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          00                               .       
```

#### Opcodes

```
  0: 0x0068 [0x00] END_REQSTACK()
```

### Event 5084

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             00                             .      
```

#### Opcodes

```
  0: 0x0069 [0x00] END_REQSTACK()
```

### Event 5085

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 5086

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   00                         .    
```

#### Opcodes

```
  0: 0x006B [0x00] END_REQSTACK()
```
