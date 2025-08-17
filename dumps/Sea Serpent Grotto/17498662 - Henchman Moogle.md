# 17498662 - Henchman Moogle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Sea Serpent Grotto (ID: 176) |
| Block Size       | 104 bytes                    |
| Total Events     | 6                            |
| References Count | 2                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [19](#event-19)          | 0x0001       |      1 |              1 |
| [22](#event-22)          | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     19 |              5 |
| [65535.2](#event-655352) | 0x0016       |     16 |              2 |
| [65535.3](#event-655353) | 0x0026       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x093C      |        2364 |
|       1 | 0x0A4C      |        2636 |

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

### Event 19

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

### Event 22

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
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          22 00 B6 00 00  80 92 01 F8 FF FF 7F 94     "............
0010: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0003 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0005 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2364*)
  2: 0x0009 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x94] EventEntity->Render.Flags3 ^= 0x01
  4: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   5B 01  80 F8 FF FF 7F F8 FF FF        [.........
0020: 7F 74 6C 6B 30 00                                 .tlk0.          
```

#### Opcodes

```
  0: 0x0016 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   5B 01  80 F8 FF FF 7F F8 FF FF        [.........
0030: 7F 73 74 64 30 00                                 .std0.          
```

#### Opcodes

```
  0: 0x0026 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "std0" with entities [EventEntity, EventEntity], work=2636*
  1: 0x0035 [0x00] END_REQSTACK()
```
