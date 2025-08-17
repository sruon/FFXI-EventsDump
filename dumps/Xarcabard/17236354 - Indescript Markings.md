# 17236354 - Indescript Markings

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Xarcabard (ID: 112) |
| Block Size       | 56 bytes            |
| Total Events     | 4                   |
| References Count | 2                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [44](#event-44)       | 0x0001       |      1 |              1 |
| [46](#event-46)       | 0x0002       |      1 |              1 |
| [45](#event-45)       | 0x0003       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x09FD      |        2557 |
|       1 | 0x1FB6      |        8118 |

## String References

- **8118**: The formula of porting has been laid out. After securing $0, it should transport you to the royal tomb.

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

### Event 44

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

### Event 46

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

### Event 45

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          03 02 10 00 80  48 01 80 23 21 00           .....H..#!.  
```

#### Opcodes

```
  0: 0x0003 [0x03] Work_Zone[2] = 2557*
  1: 0x0008 [0x48] [System] [8118*]:
    → "The formula of porting has been laid out. After securing $0, it should transport you to the royal tomb."
  2: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000C [0x21] END_EVENT
  4: 0x000D [0x00] END_REQSTACK()
```
