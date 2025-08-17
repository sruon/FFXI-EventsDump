# 17764557 - DoorManustery

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 72 bytes                 |
| Total Events     | 9                        |
| References Count | 1                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [308](#event-308)        | 0x0001       |      1 |              1 |
| [314](#event-314)        | 0x0002       |      1 |              1 |
| [600](#event-600)        | 0x0003       |      2 |              2 |
| [319](#event-319)        | 0x0005       |      1 |              1 |
| [325](#event-325)        | 0x0006       |      1 |              1 |
| [392](#event-392)        | 0x0007       |      1 |              1 |
| [619](#event-619)        | 0x0008       |      1 |              1 |
| [65535.1](#event-655351) | 0x0009       |      6 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |

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

### Event 308

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

### Event 314

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

### Event 600

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4D 00                                       M.           
```

#### Opcodes

```
  0: 0x0003 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 319

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

### Event 325

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

### Event 392

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

### Event 619

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          00                               .       
```

#### Opcodes

```
  0: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             4C 1C 00 80 4D 00              L...M. 
```

#### Opcodes

```
  0: 0x0009 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x000A [0x1C] WAIT(200* ticks)
  2: 0x000D [0x4D] EventEntity->StatusEvent = 9 // Close door
  3: 0x000E [0x00] END_REQSTACK()
```
