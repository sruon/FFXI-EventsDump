# 17814100 - Lumber Chest

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 60 bytes                       |
| Total Events     | 3                              |
| References Count | 2                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [278](#event-278)     | 0x0001       |     12 |              6 |
| [279](#event-279)     | 0x000D       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x06B6      |        1718 |
|       1 | 0x1EF8      |        7928 |

## String References

- **7928**: It is stocked to the brim with $5.

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

### Event 278

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 10 00 80 42 48  01 80 23 21 00            .....BH..#!.   
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[2] = 1718*
  1: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0007 [0x48] [System] [7928*]:
    → "It is stocked to the brim with $5."
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x21] END_EVENT
  5: 0x000C [0x00] END_REQSTACK()
```

### Event 279

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         03 02 10               ...
0010: 00 80 48 01 80 23 21 00                           ..H..#!.        
```

#### Opcodes

```
  0: 0x000D [0x03] Work_Zone[2] = 1718*
  1: 0x0012 [0x48] [System] [7928*]:
    → "It is stocked to the brim with $5."
  2: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0016 [0x21] END_EVENT
  4: 0x0017 [0x00] END_REQSTACK()
```
