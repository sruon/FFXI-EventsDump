# 17867237 - Gramk-Droog

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 160 bytes                |
| Total Events     | 10                       |
| References Count | 11                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [54](#event-54)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |
| [55](#event-55)          | 0x0018       |      1 |              1 |
| [57](#event-57)          | 0x0019       |      1 |              1 |
| [65535.2](#event-655352) | 0x001A       |      5 |              2 |
| [65535.3](#event-655353) | 0x001F       |      5 |              2 |
| [65](#event-65)          | 0x0024       |      5 |              2 |
| [65535.4](#event-655354) | 0x0029       |     14 |              4 |
| [66](#event-66)          | 0x0037       |      5 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE4D2A  |  4294855978 |
|       2 | 0xFFFEC4EE  |  4294886638 |
|       3 | 0x4F08      |       20232 |
|       4 | 0x0153      |         339 |
|       5 | 0x0A1E      |        2590 |
|       6 | 0x0AB1      |        2737 |
|       7 | 0x0032      |          50 |
|       8 | 0xE910      |       59664 |
|       9 | 0xFFFE968D  |  4294874765 |
|      10 | 0x50B1      |       20657 |

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

### Event 54

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 4B F8 FF FF 7F 04 80 00                           K.......        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-111.318*, Z=-80.658*, Y=20.232*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=1.9°*)
  5: 0x0017 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0018  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          00                               .       
```

#### Opcodes

```
  0: 0x0018 [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             00                             .      
```

#### Opcodes

```
  0: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                B6 00 05 80 00               ..... 
```

#### Opcodes

```
  0: 0x001A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2590*)
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               B6                 .
0020: 00 06 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2737*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 05 80  00                           .....       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2590*)
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             32 07 80 1F 00 08 80           2......
0030: 09 80 0A 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0029 [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  1: 0x002C [0x1F] MOVE_ENTITY: EventEntity moves to X=59.664*, Z=-92.531*, Y=20.657*
  2: 0x0034 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0036 [0x00] END_REQSTACK()
```

### Event 66

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      B6  00 05 80 00                     .....    
```

#### Opcodes

```
  0: 0x0037 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2590*)
  1: 0x003B [0x00] END_REQSTACK()
```
