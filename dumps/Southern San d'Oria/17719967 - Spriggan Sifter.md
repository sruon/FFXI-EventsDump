# 17719967 - Spriggan Sifter

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 52 bytes                      |
| Total Events     | 6                             |
| References Count | 0                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [3508](#event-3508)      | 0x0001       |      3 |              2 |
| [3509](#event-3509)      | 0x0004       |      1 |              1 |
| [3510](#event-3510)      | 0x0005       |      1 |              1 |
| [3511](#event-3511)      | 0x0006       |      1 |              1 |
| [65535.1](#event-655351) | 0x0007       |      4 |              2 |

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

### Event 3508

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    A4 01 00                                        ...            
```

#### Opcodes

```
  0: 0x0001 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 3509

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

### Event 3510

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

### Event 3511

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
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      1C  07 17 00                        ....     
```

#### Opcodes

```
  0: 0x0007 [0x1C] WAIT(Work_Zone_1700[7] ticks)
  1: 0x000A [0x00] END_REQSTACK()
```
