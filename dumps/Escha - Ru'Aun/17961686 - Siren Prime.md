# 17961686 - Siren Prime

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Escha - Ru'Aun (ID: 289) |
| Block Size       | 68 bytes                 |
| Total Events     | 6                        |
| References Count | 2                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      1 |              1 |
| [5](#event-5)            | 0x0002       |      5 |              2 |
| [7](#event-7)            | 0x0007       |      5 |              2 |
| [65535.1](#event-655351) | 0x000C       |      5 |              2 |
| [9](#event-9)            | 0x0011       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0146      |         326 |
|       1 | 0x0996      |        2454 |

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

### Event 4

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

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 00 00 80 00                                .....         
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=326*)
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      B6  00 00 80 00                     .....    
```

#### Opcodes

```
  0: 0x0007 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=326*)
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      B6 00 01 80              ....
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2454*)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```
