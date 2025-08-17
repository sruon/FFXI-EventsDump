# 17469815 - Talking Doll

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 168 bytes                  |
| Total Events     | 12                         |
| References Count | 11                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [42](#event-42)       | 0x0001       |      1 |              1 |
| [43](#event-43)       | 0x0002       |      1 |              1 |
| [44](#event-44)       | 0x0003       |      1 |              1 |
| [52](#event-52)       | 0x0004       |     16 |              3 |
| [45](#event-45)       | 0x0014       |      1 |              1 |
| [46](#event-46)       | 0x0015       |      1 |              1 |
| [47](#event-47)       | 0x0016       |      1 |              1 |
| [53](#event-53)       | 0x0017       |     16 |              3 |
| [48](#event-48)       | 0x0027       |      1 |              1 |
| [55](#event-55)       | 0x0028       |      1 |              1 |
| [54](#event-54)       | 0x0029       |     16 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDEA48  |  4294830664 |
|       1 | 0x246E4     |      149220 |
|       2 | 0x3E7F      |       15999 |
|       3 | 0x0AD0      |        2768 |
|       4 | 0xFFFE8C63  |  4294872163 |
|       5 | 0xFFFF8C58  |  4294937688 |
|       6 | 0x037F      |         895 |
|       7 | 0x4B2B      |       19243 |
|       8 | 0xEB7A      |       60282 |
|       9 | 0x4267      |       16999 |
|      10 | 0x02B6      |         694 |

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

### Event 42

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

### Event 43

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

### Event 44

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 52

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4E 00 77 91  0A 01 37 00 80 01 80 02      N.w...7.....
0010: 80 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0004 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17469815/0x010A9177)
  1: 0x000A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-136.632*, z=149.220*, y=15.999*, direction=243.3°*
  2: 0x0013 [0x00] END_REQSTACK()
```

### Event 45

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             00                                        .           
```

#### Opcodes

```
  0: 0x0014 [0x00] END_REQSTACK()
```

### Event 46

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                00                                      .          
```

#### Opcodes

```
  0: 0x0015 [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   00                                    .         
```

#### Opcodes

```
  0: 0x0016 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      4E  00 77 91 0A 01 37 04 80         N.w...7..
0020: 05 80 02 80 06 80 00                              .......         
```

#### Opcodes

```
  0: 0x0017 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17469815/0x010A9177)
  1: 0x001D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-95.133*, z=-29.608*, y=15.999*, direction=78.7°*
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      00                                  .        
```

#### Opcodes

```
  0: 0x0027 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```

### Event 54

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             4E 00 77 91 0A 01 37           N.w...7
0030: 07 80 08 80 09 80 0A 80  00                       .........       
```

#### Opcodes

```
  0: 0x0029 [0x4E] SET_ENTITY_HIDE_FLAG: Show Talking Doll (ID: 17469815/0x010A9177)
  1: 0x002F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=19.243*, z=60.282*, y=16.999*, direction=61.0°*
  2: 0x0038 [0x00] END_REQSTACK()
```
