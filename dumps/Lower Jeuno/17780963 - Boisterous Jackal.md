# 17780963 - Boisterous Jackal

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 88 bytes              |
| Total Events     | 9                     |
| References Count | 2                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10126](#event-10126)    | 0x0001       |      1 |              1 |
| [10127](#event-10127)    | 0x0002       |      1 |              1 |
| [10128](#event-10128)    | 0x0003       |      1 |              1 |
| [10129](#event-10129)    | 0x0004       |      1 |              1 |
| [10132](#event-10132)    | 0x0005       |      1 |              1 |
| [10133](#event-10133)    | 0x0006       |      1 |              1 |
| [65535.1](#event-655351) | 0x0007       |      7 |              3 |
| [65535.2](#event-655352) | 0x000E       |     13 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |

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

### Event 10126

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

### Event 10127

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

### Event 10128

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

### Event 10129

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

### Event 10132

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0005  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                00                                      .          
```

#### Opcodes

```
  0: 0x0005 [0x00] END_REQSTACK()
```

### Event 10133

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0006  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   00                                    .         
```

#### Opcodes

```
  0: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      AB  03 AC 01 00 80 00               .......  
```

#### Opcodes

```
  0: 0x0007 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0009 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            7A 05                z.
0010: F8 FF FF 7F AC 01 01 80  AB 04 00                 ...........     
```

#### Opcodes

```
  0: 0x000E [0x7A] VM_CONTROL: Reset copy state for EventEntity
  1: 0x0014 [0xAC] EventEntity->StatusEvent = 0*
  2: 0x0018 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  3: 0x001A [0x00] END_REQSTACK()
```
