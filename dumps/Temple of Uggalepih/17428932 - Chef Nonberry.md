# 17428932 - Chef Nonberry

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 56 bytes                      |
| Total Events     | 3                             |
| References Count | 2                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [27](#event-27)       | 0x0001       |      9 |              6 |
| [28](#event-28)       | 0x000A       |      9 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D1E      |        7454 |
|       1 | 0x1D1D      |        7453 |

## String References

- **7453**: Chop! Chop!! Chop!!! Chop!!!!
- **7454**: Chop... Chop...... Chop......... Can't cut!!!

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

### Event 27

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 9 bytes |
| Instructions | 6       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1D 00 80 23 20 00  21 00                     B...# .!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1D] PRINT_EVENT_MESSAGE(message_id=7454*)
    → "Chop... Chop...... Chop......... Can't cut!!!"
  2: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x0008 [0x21] END_EVENT
  5: 0x0009 [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 9 bytes |
| Instructions | 6       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                42 1D 01 80 23 20            B...# 
0010: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7453*)
    → "Chop! Chop!! Chop!!! Chop!!!!"
  2: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x0011 [0x21] END_EVENT
  5: 0x0012 [0x00] END_REQSTACK()
```
