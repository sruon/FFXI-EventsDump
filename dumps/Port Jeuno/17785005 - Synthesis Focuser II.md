# 17785005 - Synthesis Focuser II

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 64 bytes             |
| Total Events     | 7                    |
| References Count | 0                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [426](#event-426)     | 0x0001       |      1 |              1 |
| [427](#event-427)     | 0x0002       |      1 |              1 |
| [428](#event-428)     | 0x0003       |      1 |              1 |
| [431](#event-431)     | 0x0004       |      1 |              1 |
| [434](#event-434)     | 0x0005       |      7 |              2 |
| [432](#event-432)     | 0x000C       |      7 |              2 |

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

### Event 426

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

### Event 427

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

### Event 428

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

### Event 431

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 434

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0005 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 432

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      92 01 F8 FF              ....
0010: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x000C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0012 [0x00] END_REQSTACK()
```
