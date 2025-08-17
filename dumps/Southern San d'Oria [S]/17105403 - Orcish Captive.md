# 17105403 - Orcish Captive

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 60 bytes                         |
| Total Events     | 6                                |
| References Count | 1                                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [21](#event-21)          | 0x0001       |      1 |              1 |
| [22](#event-22)          | 0x0002       |      1 |              1 |
| [609](#event-609)        | 0x0003       |      6 |              4 |
| [65535.1](#event-655351) | 0x0009       |      3 |              2 |
| [65535.2](#event-655352) | 0x000C       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2F4C      |       12108 |

## String References

- **12108**: Bakgodek vegbreg... Come soon... You die all...

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

### Event 21

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

### Event 609

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          1D 00 80 23 21  00                          ...#!.       
```

#### Opcodes

```
  0: 0x0003 [0x1D] PRINT_EVENT_MESSAGE(message_id=12108*)
    → "Bakgodek vegbreg... Come soon... You die all..."
  1: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0007 [0x21] END_EVENT
  3: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             A5 00 00                       ...    
```

#### Opcodes

```
  0: 0x0009 [0xA5] EventEntity->Flags3.BallistaTeam &= ~0x08  // Clear bit 3 of BallistaTeam
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      A5 01 00                 ... 
```

#### Opcodes

```
  0: 0x000C [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  1: 0x000E [0x00] END_REQSTACK()
```
